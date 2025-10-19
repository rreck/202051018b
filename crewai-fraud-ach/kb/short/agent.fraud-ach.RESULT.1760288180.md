```json
{
  "id": "14652c0f9bd38718",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288180,
  "host_pid": "9e6742732c60:1",
  "hash": "16f04a1249a1f2fbb4df5453e83f5c9d176ee4050ae9e96ba01c785ffb93004b",
  "cid": "QmV116f04a1249a1f2fbb4df5453e83f5c9d176ee405",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288180,
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
      "evaluated_at": 1760288180
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
  "sig": "1b0f2d40b34749fdb584c9599d132aedd1af651a26ad390ae3097c77a72571cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155322765
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 36531895, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285763, 'matching_hash': '7a27d1bb592c5069'}}}