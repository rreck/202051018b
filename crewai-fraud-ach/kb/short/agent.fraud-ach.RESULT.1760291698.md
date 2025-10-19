```json
{
  "id": "86c2e64f689d819e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291698,
  "host_pid": "9e6742732c60:1",
  "hash": "88c9ec02dede937cf669688a86164248a661642fb5e4acbca4b888aa219eea12",
  "cid": "QmV188c9ec02dede937cf669688a86164248a661642f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291698,
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
      "evaluated_at": 1760291698
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
  "sig": "108edd818b0d900a3ce35fdd58162157f5941279761b5c3ec5d22030cd122578"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024349722
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 11769887, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '3e275568f5204778'}}}