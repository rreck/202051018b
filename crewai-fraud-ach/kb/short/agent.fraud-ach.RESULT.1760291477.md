```json
{
  "id": "085ae77fd704891c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291477,
  "host_pid": "9e6742732c60:1",
  "hash": "f045c39d583f51aef2746970c67358eb9d098bc529c30a4494aace6a30cf1d3e",
  "cid": "QmV1f045c39d583f51aef2746970c67358eb9d098bc5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291477,
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
      "evaluated_at": 1760291477
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
  "sig": "6d66995a8b68084a8f879b7f0ad0957c56ab70830969f3f51d201845f5c6f154"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279650502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 43904784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': 'f07ec2819f69af8b'}}}