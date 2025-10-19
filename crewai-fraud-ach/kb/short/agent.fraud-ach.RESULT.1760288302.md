```json
{
  "id": "a23a635587f41c78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288302,
  "host_pid": "9e6742732c60:1",
  "hash": "f28ea1349ecd1d13673ec5c5635734062c548a43856290ce9d6a45ab5225f70c",
  "cid": "QmV1f28ea1349ecd1d13673ec5c5635734062c548a43",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288302,
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
      "evaluated_at": 1760288302
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
  "sig": "7b5706a46d782f2937474cc08f9c03766f3c151568c04dc220ecaae186caf57e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024421000
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 40256035, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': 'ab9abea401ffdb4a'}}}