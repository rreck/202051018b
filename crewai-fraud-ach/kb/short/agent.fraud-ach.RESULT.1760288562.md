```json
{
  "id": "ddda05d888ecc5b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288562,
  "host_pid": "9e6742732c60:1",
  "hash": "d60d4bfe3acf7017465bfcd3e7bc8927d9b403ba15fe9532af289c9f462cb856",
  "cid": "QmV1d60d4bfe3acf7017465bfcd3e7bc8927d9b403ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288562,
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
      "evaluated_at": 1760288562
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
  "sig": "1b9dcb5c40f0e59442163a45690b7d1e6dfbe6a609892d05bf08ab167a634067"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465763935
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 38478930, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285763, 'matching_hash': '9c229bcc2f82b898'}}}