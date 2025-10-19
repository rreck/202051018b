```json
{
  "id": "abae2a3d09732fe7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288561,
  "host_pid": "9e6742732c60:1",
  "hash": "afb489e51fd1fdaf3853349595c9ba7d6add4bca1fe976d13da174ff94ea1cc5",
  "cid": "QmV1afb489e51fd1fdaf3853349595c9ba7d6add4bca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288561,
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
      "evaluated_at": 1760288561
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
  "sig": "b81e7d297075015d75ad35a4f0c31e9c2313986404fe7296a481928054ef3104"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274268796
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 25137259, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285763, 'matching_hash': 'ac75b07ed83ae58c'}}}