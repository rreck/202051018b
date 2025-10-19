```json
{
  "id": "f911397f65d80481",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293260,
  "host_pid": "9e6742732c60:1",
  "hash": "cdbdbf358233a5c86de6e13b9b0a1433d5b98106952cf087bde09cff180ddb3d",
  "cid": "QmV1cdbdbf358233a5c86de6e13b9b0a1433d5b98106",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293260,
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
      "evaluated_at": 1760293260
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
  "sig": "cd2606ae7a787b111745894b5bc4b8bb84b6cbe2158d58ed99e0b0afa2b1d517"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025759024
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 82287165, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': 'fa026da4c6071776'}}}