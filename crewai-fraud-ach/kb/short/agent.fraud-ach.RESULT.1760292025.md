```json
{
  "id": "f9bbe52c6640dac8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292025,
  "host_pid": "9e6742732c60:1",
  "hash": "c4363807d736de16ebaf338237d01c7d4819ad8387dfe0434ba4a5888b845ef8",
  "cid": "QmV1c4363807d736de16ebaf338237d01c7d4819ad83",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292025,
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
      "evaluated_at": 1760292025
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
  "sig": "a24af237538fbe9e14b307692f2d772128621bec08f2940eaf55a5833d161ab6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155194168
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 68741260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285765, 'matching_hash': '7ab74b64ae25594e'}}}