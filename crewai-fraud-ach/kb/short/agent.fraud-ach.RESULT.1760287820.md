```json
{
  "id": "6d28ff3fba754d2d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287820,
  "host_pid": "9e6742732c60:1",
  "hash": "1300c77082ea2f87165744ab1cd8ca4a84c2308cdac45a0a629021ba5a4b3437",
  "cid": "QmV11300c77082ea2f87165744ab1cd8ca4a84c2308c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287820,
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
      "evaluated_at": 1760287820
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
  "sig": "9b9e91d008c386e929cec85bd2f15659135d6b01124d0c7792f07898081f2e89"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 044000037652029
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 20829382, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285765, 'matching_hash': '6ae01c61248929d6'}}}