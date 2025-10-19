```json
{
  "id": "a891ba58f84e2a8f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290947,
  "host_pid": "9e6742732c60:1",
  "hash": "f89d484ec2d49d87d6a7819029ff199d2054b6f8d5cfc75ced7eb4fc330bfbc7",
  "cid": "QmV1f89d484ec2d49d87d6a7819029ff199d2054b6f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290947,
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
      "evaluated_at": 1760290947
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
  "sig": "48672c67511bd49141ed6e1ef27b577b1c21ab72dc1736cbd8288a7b4e191967"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 63109862, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}