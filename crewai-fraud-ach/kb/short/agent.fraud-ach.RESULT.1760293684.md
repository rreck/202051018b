```json
{
  "id": "7a4a8a9a8cb367b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293684,
  "host_pid": "9e6742732c60:1",
  "hash": "a7d086df4578c1ae4f42b379b797544efcfe326d99d59df840eaa1390af2bed5",
  "cid": "QmV1a7d086df4578c1ae4f42b379b797544efcfe326d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293684,
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
      "evaluated_at": 1760293684
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
  "sig": "8d79b65f6adb93833ce24675eb458fa3b69f33d263d84daa9666de881929b327"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590909791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 21140177, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285765, 'matching_hash': 'dd7dbd0f0c1d6f0c'}}}