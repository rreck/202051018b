```json
{
  "id": "8dae898f3cabea91",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286366,
  "host_pid": "9e6742732c60:1",
  "hash": "4aae9d124946ef69679442892ea0193659f6664fe4417891f603b7d9dc2080eb",
  "cid": "QmV14aae9d124946ef69679442892ea0193659f6664f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286366,
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
      "evaluated_at": 1760286366
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
  "sig": "c4e3b00fbcc655850d8bb2017376eef1916d744fa40aee86352946d637c16572"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 122105158962917
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 23000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285763, 'matching_hash': '11dc2cfd2eb8ef5d'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}