```json
{
  "id": "46d1ccfbfff6de56",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290303,
  "host_pid": "9e6742732c60:1",
  "hash": "cbb7dafa054bd246531eca375e3e10871fe0f16cf3e19c4504adb14b92715dd3",
  "cid": "QmV1cbb7dafa054bd246531eca375e3e10871fe0f16c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290303,
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
      "evaluated_at": 1760290303
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
  "sig": "567023be739f7434af7b0ee0fdbe4e90495bb267f73235aa2d47283a4d3580c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247483978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 39542265, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': '670c0389f5bcb489'}}}