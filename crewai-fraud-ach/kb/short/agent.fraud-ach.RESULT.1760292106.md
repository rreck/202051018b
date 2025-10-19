```json
{
  "id": "973168bd34448829",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292106,
  "host_pid": "9e6742732c60:1",
  "hash": "7cb4faf5cddfd79233b29f96fbb5f10423f236f5460b4bc9c7869dfbcfcecd9a",
  "cid": "QmV17cb4faf5cddfd79233b29f96fbb5f10423f236f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292106,
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
      "evaluated_at": 1760292106
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
  "sig": "664ed2c9a4dec6dc8140ee909aa33cb7ceb4ef7df82a3e00c80b19508ef8a5df"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027064013
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 56550460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285765, 'matching_hash': '811cb7a859f68158'}}}