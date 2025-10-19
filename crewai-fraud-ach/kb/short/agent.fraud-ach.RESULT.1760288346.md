```json
{
  "id": "1ee003493e52fd77",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288346,
  "host_pid": "9e6742732c60:1",
  "hash": "223de0f189f1685ed06594dd303e0b24b6e946103dc89e557616fed9d7a6b47d",
  "cid": "QmV1223de0f189f1685ed06594dd303e0b24b6e94610",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288346,
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
      "evaluated_at": 1760288346
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
  "sig": "917a456190fb801013a087f72ed141c9684cf773edb6c507d3d4358ab71a1bc9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 28129590, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}