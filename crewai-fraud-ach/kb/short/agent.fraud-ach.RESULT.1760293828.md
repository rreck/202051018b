```json
{
  "id": "934d63baf39b84ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293828,
  "host_pid": "9e6742732c60:1",
  "hash": "7382450b93ff0091822dc896b75ba1442b001c0d25f16379f4421f2fdf086dad",
  "cid": "QmV17382450b93ff0091822dc896b75ba1442b001c0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293828,
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
      "evaluated_at": 1760293828
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
  "sig": "1fd98020b47faee480d5f914bab7e7b436094792e2e8bd51183b48467a62ba42"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026132147
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 40994818, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285765, 'matching_hash': 'fe0c58008e192989'}}}