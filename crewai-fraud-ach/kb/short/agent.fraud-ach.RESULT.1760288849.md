```json
{
  "id": "69efde21e77b3c4c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288849,
  "host_pid": "9e6742732c60:1",
  "hash": "df88638581909b8007528afd5704f098a84a1e3e1a7881c68f070d3e87aa3944",
  "cid": "QmV1df88638581909b8007528afd5704f098a84a1e3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288849,
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
      "evaluated_at": 1760288849
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
  "sig": "60c31ef95cc5656d2782268b81fe61e89112cbfba67030d8cfd213bdf970eee2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026239341
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 44897996, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '200fd923cb07cfcf'}}}