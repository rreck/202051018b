```json
{
  "id": "fdfc86a402b92e83",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292954,
  "host_pid": "9e6742732c60:1",
  "hash": "b06f641f6743b1e5dba6e3a2e117639df812968a35affd39f50e415e410b6372",
  "cid": "QmV1b06f641f6743b1e5dba6e3a2e117639df812968a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292954,
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
      "evaluated_at": 1760292954
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
  "sig": "b3d17e332dc63e00e89c12b87a3a2e9fa56b221a10e19dd906db827ca4e194e2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461662832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 86929856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': 'adb809538e6eb6af'}}}