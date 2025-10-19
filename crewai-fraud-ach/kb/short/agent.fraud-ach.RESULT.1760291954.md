```json
{
  "id": "9b890d37f9494624",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291954,
  "host_pid": "9e6742732c60:1",
  "hash": "8b2d0d8da83737ad069d7193974b949f08680fe68358cacda3c8554a4ce62322",
  "cid": "QmV18b2d0d8da83737ad069d7193974b949f08680fe6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291954,
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
      "evaluated_at": 1760291954
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
  "sig": "bcbfedab3e549fc52c3efd60bc3dca23efd392352f24a743c902f5903ac853e9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159848459
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 38527984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': 'f6f76290fac8b474'}}}