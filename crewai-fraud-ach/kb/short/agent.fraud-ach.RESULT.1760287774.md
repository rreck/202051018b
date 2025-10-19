```json
{
  "id": "fa73b41a30d5349d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287774,
  "host_pid": "9e6742732c60:1",
  "hash": "0728f35cd276adb89ceea26eb16e399a09db82cc091379a1c8a4a68352ff63c7",
  "cid": "QmV10728f35cd276adb89ceea26eb16e399a09db82cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287774,
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
      "evaluated_at": 1760287774
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
  "sig": "cdafe03bed66d6a3f35f0ccdf66cc1093153947a7a3ac93616b21648bf1cbfd6"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 063100271052795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 15883776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285763, 'matching_hash': '457d955844db0007'}}}