```json
{
  "id": "654dbfbdf96e8bcc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292276,
  "host_pid": "9e6742732c60:1",
  "hash": "4c82c870ee52604cfc4519d46064077c18ed246083768559f6718ab6def7d3ad",
  "cid": "QmV14c82c870ee52604cfc4519d46064077c18ed2460",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292276,
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
      "evaluated_at": 1760292276
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
  "sig": "705dc7eb6c77eab0bc0afcbb1c505328c9d6bd4497fadb2bce7ad997db12efee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274521172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 20680788, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285764, 'matching_hash': 'cfb56b896e519b42'}}}