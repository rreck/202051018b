```json
{
  "id": "53013f167c1bff47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287853,
  "host_pid": "9e6742732c60:1",
  "hash": "0dda2d7f085e7e4b21c87390661ae8583aebb54d8f544821641a39e5004cc0fb",
  "cid": "QmV10dda2d7f085e7e4b21c87390661ae8583aebb54d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287853,
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
      "evaluated_at": 1760287853
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
  "sig": "e88b542460ab5ee02c2944a09deaeae34ac87f95254107ffa01f2fbf75fcb5ce"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 021000025329406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 35840198, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285765, 'matching_hash': '4bb9b304f38123bb'}}}