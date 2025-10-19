```json
{
  "id": "b52ef499885c1070",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289613,
  "host_pid": "9e6742732c60:1",
  "hash": "7fecaf727e47b1215a8887afa5d692705400844c4c6865a683b68cfb3e0d8d42",
  "cid": "QmV17fecaf727e47b1215a8887afa5d692705400844c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289613,
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
      "evaluated_at": 1760289613
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
  "sig": "595393db6b7589d5138c3ca128b92fb1b631af4034f62f292e1601f450a1c582"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154102308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 75159108, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760284979, 'matching_hash': '687d8a253912c530'}}}