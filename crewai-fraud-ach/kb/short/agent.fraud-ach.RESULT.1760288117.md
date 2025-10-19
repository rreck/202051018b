```json
{
  "id": "e1dd993c8ac391df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288117,
  "host_pid": "9e6742732c60:1",
  "hash": "8eac53db76ca1a6ca76f522b38e96b93a9e059be61ec77056b50b1cab0e65119",
  "cid": "QmV18eac53db76ca1a6ca76f522b38e96b93a9e059be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288117,
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
      "evaluated_at": 1760288117
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
  "sig": "7ce604794b3ad0161fcc51e7c3b28e3ea0edacc0413d56b0dd535052369c64c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154887163
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 55936041, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760284979, 'matching_hash': '445784114b53d57b'}}}