```json
{
  "id": "626a6fc13ff378b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293568,
  "host_pid": "9e6742732c60:1",
  "hash": "36056920ef7f5748b98b499e4ce039e3d7afa2cb92a65b7ae582c86a29a53118",
  "cid": "QmV136056920ef7f5748b98b499e4ce039e3d7afa2cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293568,
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
      "evaluated_at": 1760293568
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
  "sig": "b4767ad8ba34376d726ed8f6b5602923df17bfe4667cd6805f45f60cddede3c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153425339
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 97660342, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'd6fcd27194bc1174'}}}