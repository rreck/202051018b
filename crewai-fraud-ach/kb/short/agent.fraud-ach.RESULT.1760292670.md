```json
{
  "id": "33ee126c39696600",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292670,
  "host_pid": "9e6742732c60:1",
  "hash": "ef97e4ebc1685494411f4360d5fc8064d0a0af87743bef32c05dac8fb4d51a7b",
  "cid": "QmV1ef97e4ebc1685494411f4360d5fc8064d0a0af87",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292670,
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
      "evaluated_at": 1760292670
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
  "sig": "3ab0287ae54bb9fb9bb3c5df0a0b8410f1e903e0662e64690667931025035658"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 64286096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}