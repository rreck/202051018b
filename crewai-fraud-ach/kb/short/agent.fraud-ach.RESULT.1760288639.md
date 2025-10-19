```json
{
  "id": "5ed94a0fc1854321",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288639,
  "host_pid": "9e6742732c60:1",
  "hash": "d08658f34d7fbe0aa2425c028ea15351001aaa4de258b4d1d37ebcf2143f7367",
  "cid": "QmV1d08658f34d7fbe0aa2425c028ea15351001aaa4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288639,
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
      "evaluated_at": 1760288639
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
  "sig": "6dda55d229ca1c593bc7b5f5fcaf652c96efc89a9ef2d74035b06bf486c9ed92"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 24750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285765, 'matching_hash': '9c2417d6ee361cba'}}}