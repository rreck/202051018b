```json
{
  "id": "c2eda9e92d6307c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287823,
  "host_pid": "9e6742732c60:1",
  "hash": "b082fb251e27f067e66a8da6a9e70e7412006779da82e06eae61cd2a73c56054",
  "cid": "QmV1b082fb251e27f067e66a8da6a9e70e7412006779",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287823,
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
      "evaluated_at": 1760287823
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "f782a725c53eef79d550ad30570a702cadd2fbb2d15679f8bd9fbad98d6b63ca"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 122105155958228
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 30772566, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285765, 'matching_hash': '1e57f627a6d207f5'}}}