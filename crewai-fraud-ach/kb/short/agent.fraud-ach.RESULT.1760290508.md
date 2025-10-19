```json
{
  "id": "5e647c470a41da1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290508,
  "host_pid": "9e6742732c60:1",
  "hash": "6b8365494a7e82322d81afce9afe1d6a63c4adde4b1f5e55c093da3f0f254898",
  "cid": "QmV16b8365494a7e82322d81afce9afe1d6a63c4adde",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290508,
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
      "evaluated_at": 1760290508
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
  "sig": "6213c445d9e080449bf27cad3fa133caf88243600efc750111ac583373868b70"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026682072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 51098600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285764, 'matching_hash': 'ef2983ea6f6c1303'}}}