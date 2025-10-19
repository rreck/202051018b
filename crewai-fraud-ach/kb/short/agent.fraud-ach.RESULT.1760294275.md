```json
{
  "id": "d7ff3a8aae898590",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294275,
  "host_pid": "9e6742732c60:1",
  "hash": "b180ca959ab91a817366ec2f014daeed1d715d86d5280c07e67de32c235099b0",
  "cid": "QmV1b180ca959ab91a817366ec2f014daeed1d715d86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294275,
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
      "evaluated_at": 1760294275
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
  "sig": "60b948e1d53de20afc2464165532eefe120f4ba9917aa560cb7a4de081935966"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277276019
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 88825065, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '90b38bd8812494f9'}}}