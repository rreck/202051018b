```json
{
  "id": "d63ae4a5333e9d56",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292020,
  "host_pid": "9e6742732c60:1",
  "hash": "eed04ffbd738acfe687523dbc55ef45db9c774790ddb6ea944174cb16e66578d",
  "cid": "QmV1eed04ffbd738acfe687523dbc55ef45db9c77479",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292020,
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
      "evaluated_at": 1760292020
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
  "sig": "e40b37556eb1c59165860c64deb0da36cd7a183e17205ffad0afe5792bfaebf1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594283807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 37895348, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285764, 'matching_hash': 'e41bbca7fc0ba663'}}}