```json
{
  "id": "ecbe118a0a05c484",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293258,
  "host_pid": "9e6742732c60:1",
  "hash": "fcdd1668cd8ce26029598c1fd326a91c3fba22bd9b52827017425357795b9d76",
  "cid": "QmV1fcdd1668cd8ce26029598c1fd326a91c3fba22bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293258,
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
      "evaluated_at": 1760293259
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
  "sig": "dc542da6c955078059b74ba081b6a59a301e4823cccdda3883d3570204630140"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591682020
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 62566075, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '594333c81206e179'}}}