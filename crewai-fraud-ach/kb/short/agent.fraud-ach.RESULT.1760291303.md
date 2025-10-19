```json
{
  "id": "8bd893a1128e7756",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291303,
  "host_pid": "9e6742732c60:1",
  "hash": "d820fac753116e2560af2c05b3406cd88548057f749b9032883c5a9fd1c26615",
  "cid": "QmV1d820fac753116e2560af2c05b3406cd88548057f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291303,
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
      "evaluated_at": 1760291303
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
  "sig": "efde25042c9967afe283baff77a32f501eb87eae0e2c734203cd0570e0041970"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026299785
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 75613092, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': 'dc2585930aebf220'}}}