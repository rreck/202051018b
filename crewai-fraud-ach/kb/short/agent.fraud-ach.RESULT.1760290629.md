```json
{
  "id": "5d6cca73bc8f0c23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290629,
  "host_pid": "9e6742732c60:1",
  "hash": "aca7765b45d1e0c2313e8428c90b6f219c29f9c6ee307bdc91f373bd54129134",
  "cid": "QmV1aca7765b45d1e0c2313e8428c90b6f219c29f9c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290629,
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
      "evaluated_at": 1760290629
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
  "sig": "69973b933a11769bccd8adfb86b9f5deef23fd655011a6d60d7e46bb376f90b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465836827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 48357540, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760284979, 'matching_hash': '8a0ab7f0e4aa4922'}}}