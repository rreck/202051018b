```json
{
  "id": "9224217a88d4099a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291522,
  "host_pid": "9e6742732c60:1",
  "hash": "a22450b3d831d5e46dc11670f656dcaff75b929605de17f85d295dfbf953f06a",
  "cid": "QmV1a22450b3d831d5e46dc11670f656dcaff75b9296",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291522,
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
      "evaluated_at": 1760291522
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
  "sig": "1c64a1b6481a8c6e2655fad330832506c644025d4878281d96a91c3073efc6bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598219972
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 86546451, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '09b5d296b49f9602'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}