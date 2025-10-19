```json
{
  "id": "2409bea7c219a401",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292107,
  "host_pid": "9e6742732c60:1",
  "hash": "b1d2980e8c96cd4a19fb249a1130a3d34757c9c2b1463189899a0960b301f831",
  "cid": "QmV1b1d2980e8c96cd4a19fb249a1130a3d34757c9c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292107,
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
      "evaluated_at": 1760292107
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
  "sig": "1b4381e2c72d24e58954fe91cb7b8ad58911a987c0c62e7d1ff2dd06f6d19706"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037578651
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 15370430, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285763, 'matching_hash': '25cb229761d99325'}}}