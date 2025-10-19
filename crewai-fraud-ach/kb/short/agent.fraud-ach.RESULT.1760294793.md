```json
{
  "id": "50f89345e27a9322",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294793,
  "host_pid": "9e6742732c60:1",
  "hash": "732a8a4f7d7e9b2a1d691227d3cc1f23099ca26db9681d0b28b4f5493a84485d",
  "cid": "QmV1732a8a4f7d7e9b2a1d691227d3cc1f23099ca26d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294793,
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
      "evaluated_at": 1760294793
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
  "sig": "ee29a81e04e70955504f0b4ee4917c19b14ecfaa21a8357ab6f1805edccae66f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 77652512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}