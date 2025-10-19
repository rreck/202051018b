```json
{
  "id": "ef1588a068dea848",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286274,
  "host_pid": "9e6742732c60:1",
  "hash": "2419ab921e3e52c7741dbe91037e000a2cd27fe1bc7c6218c677b6d2fa414082",
  "cid": "QmV12419ab921e3e52c7741dbe91037e000a2cd27fe1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286274,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760286274
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "b6a309162a8f5e06b3ec80a4c835febecbccea376a75d3b38d6f5dfaf064ebf7"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 111000023166202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285763, 'matching_hash': 'ab99b3da8ccd3a17'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}