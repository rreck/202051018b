```json
{
  "id": "9aa437c34b1f1a44",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291487,
  "host_pid": "9e6742732c60:1",
  "hash": "55ba93152e4cabb4b66178839c0d635e8f86a63e8f842c7d11c60b98c111dc2c",
  "cid": "QmV155ba93152e4cabb4b66178839c0d635e8f86a63e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291487,
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
      "evaluated_at": 1760291487
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
  "sig": "7eda250e0f89d9c13caa038a43096d82cd7025c803d1093727e35ac7d37a61c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277214063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 50433680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': 'ff6f9f90137c8ef9'}}}