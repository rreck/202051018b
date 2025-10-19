```json
{
  "id": "cff89fd1e1a9244e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287928,
  "host_pid": "9e6742732c60:1",
  "hash": "5ae50d03349d92863edd7dcb2f8246375de4dafbcae04d779ae922978f45276c",
  "cid": "QmV15ae50d03349d92863edd7dcb2f8246375de4dafb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287928,
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
      "evaluated_at": 1760287928
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
  "sig": "73ab81a125051aae6750a3e381280397c30ea21979df32e46003948d9a4ba0ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152451584
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 30594487, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285763, 'matching_hash': '0001f0028f567562'}}}