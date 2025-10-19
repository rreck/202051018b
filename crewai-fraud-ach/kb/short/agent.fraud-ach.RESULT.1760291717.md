```json
{
  "id": "bb0746ee2fe7ad1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291717,
  "host_pid": "9e6742732c60:1",
  "hash": "2895e966721a42baa1eeeb556a20eff58f7e2dc46ddcef8c65422bcd32ddc251",
  "cid": "QmV12895e966721a42baa1eeeb556a20eff58f7e2dc4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291717,
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
      "evaluated_at": 1760291717
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
  "sig": "52ae5e29a0dd48b7c2cb846083bfd7ddf6199d75ac830db87f374b64d33cab1b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154242410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 10506869, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285765, 'matching_hash': '26a9af32f02bfdfc'}}}