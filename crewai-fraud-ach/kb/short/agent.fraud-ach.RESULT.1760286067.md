```json
{
  "id": "b7fede003e758a6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286067,
  "host_pid": "9e6742732c60:1",
  "hash": "70fdda0fefc6d753de4434f909eed4cc2729548e225eaa62a1089d6121eee815",
  "cid": "QmV170fdda0fefc6d753de4434f909eed4cc2729548e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286067,
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
      "evaluated_at": 1760286067
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
  "sig": "94eabec5ee3656c8701f9c4333ab9df1ca08097be1657b7f29e8425368846e21"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 122105156669076
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285763, 'matching_hash': '4057ff9fca3d2276'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}