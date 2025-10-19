```json
{
  "id": "cfcca773acab8673",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291227,
  "host_pid": "9e6742732c60:1",
  "hash": "ebda47a74bcbfc56fe922a0803d683e7b07df5745bb5c7d385ca76ccdcd9dbbb",
  "cid": "QmV1ebda47a74bcbfc56fe922a0803d683e7b07df574",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291227,
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
      "evaluated_at": 1760291227
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
  "sig": "eb9a3b9c31a9caccd1e275621c6f9996df8ece79f9016b027e61acc76ab03112"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278619879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 57580190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': 'bfc334a18daf8fbf'}}}