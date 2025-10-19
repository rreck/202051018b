```json
{
  "id": "eb9c4b9a826a4ab1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289733,
  "host_pid": "9e6742732c60:1",
  "hash": "172df903e5c80516a5b7234984e1f93e06ab0432bc05e906d1b797474c661ac6",
  "cid": "QmV1172df903e5c80516a5b7234984e1f93e06ab0432",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289733,
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
      "evaluated_at": 1760289733
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
  "sig": "e3beba345e8d3c328bdb4e84c5ce08c6cb51e6a31f38d382f3edfbdf4d868926"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082317
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 50466440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285765, 'matching_hash': '7a1c6367235ff38a'}}}