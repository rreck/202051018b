```json
{
  "id": "4ac9df73f1262a7e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287943,
  "host_pid": "9e6742732c60:1",
  "hash": "e27df7cc935bdc931cbb7874654a95537e5203224d4bb0711d6e0fd3b729bb47",
  "cid": "QmV1e27df7cc935bdc931cbb7874654a95537e520322",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287943,
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
      "evaluated_at": 1760287943
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
  "sig": "e66251eb36bdb2a39cdbf804a52f2f69796bfaf2ee754c35ab6edceb1c8e9cdb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155958228
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 32458734, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285765, 'matching_hash': '1e57f627a6d207f5'}}}