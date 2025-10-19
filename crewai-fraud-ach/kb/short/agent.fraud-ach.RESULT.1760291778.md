```json
{
  "id": "a206b4f175c8aa65",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291778,
  "host_pid": "9e6742732c60:1",
  "hash": "747f4b5bdeaa70a92c863953cb297e2ea163cb487002159c6ece5de8b382c5ca",
  "cid": "QmV1747f4b5bdeaa70a92c863953cb297e2ea163cb48",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291778,
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
      "evaluated_at": 1760291778
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
  "sig": "149bd63afb001bf07c15eb2555f7bb5a157c2c8afca268f03ff5cdd603445731"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000241606573
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 91500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': '2fa99cb8a6f007e0'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}