```json
{
  "id": "652e5efc39bb30b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287728,
  "host_pid": "9e6742732c60:1",
  "hash": "5547888931ee27d5aed580b1768a4fbbe387bc58f694bdca289c52cd2cd85812",
  "cid": "QmV15547888931ee27d5aed580b1768a4fbbe387bc58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287728,
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
      "evaluated_at": 1760287728
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
  "sig": "0bc831fb88c617e818313b16471c4724349a20dc28b49caa7ee8af43321e0981"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 111000029964192
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 21238350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}