```json
{
  "id": "6ea8a7cd2fdb32f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287335,
  "host_pid": "9e6742732c60:1",
  "hash": "49f97aea98e99033cf8aa429941c2046d8f75df088ec3808d055ad27ee86b511",
  "cid": "QmV149f97aea98e99033cf8aa429941c2046d8f75df0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287335,
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
      "evaluated_at": 1760287335
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "62d2d01a34f349e41f0cfef5719ebb10366ebfca535af2d1724b09fc8101c4d9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000021480535
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 27621832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285765, 'matching_hash': '9682be52dcbb3d1d'}}}