```json
{
  "id": "0ce09760b9c0b605",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286926,
  "host_pid": "9e6742732c60:1",
  "hash": "08f30acbbbb2d2e43042efab18d96f44e636fdfa58156ec4a15787c64829e598",
  "cid": "QmV108f30acbbbb2d2e43042efab18d96f44e636fdfa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286926,
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
      "evaluated_at": 1760286926
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
  "sig": "dde3f2fd4250d05abb104507da3a5a7d35094edefa0810891c517542014a81de"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 111000023166202
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 42000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285763, 'matching_hash': 'ab99b3da8ccd3a17'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}outing number checksum'}}}