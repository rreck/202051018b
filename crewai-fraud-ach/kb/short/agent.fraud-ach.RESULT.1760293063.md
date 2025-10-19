```json
{
  "id": "6df70e67679fafae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293063,
  "host_pid": "9e6742732c60:1",
  "hash": "9e85d231edda5454674579499d4932e12110453cb909fe54da637eebe08baa2a",
  "cid": "QmV19e85d231edda5454674579499d4932e12110453c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293063,
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
      "evaluated_at": 1760293063
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
  "sig": "baa88e6bfec35e716d44ca59b8f10a48816591043df862080ba0f9cc2a40f1ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155806195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 49832503, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': '37264973f9c39fe3'}}}