```json
{
  "id": "5f9c9d02be3be4bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290857,
  "host_pid": "9e6742732c60:1",
  "hash": "50d30e81fa18ed4fa75042ed6f34805290fb0662f56703bcc71f11e08ebea425",
  "cid": "QmV150d30e81fa18ed4fa75042ed6f34805290fb0662",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290857,
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
      "evaluated_at": 1760290857
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
  "sig": "3db4cd17edd61f9f098109d8e544c916fa029d0a589c7077ee440c16801bbd65"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242946545
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 26714247, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': '62b45bc192f4101a'}}}