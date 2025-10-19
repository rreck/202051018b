```json
{
  "id": "74e68febba6eb644",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286639,
  "host_pid": "9e6742732c60:1",
  "hash": "dfcf54184772144b145b987d85f5eb12644a65291b89c3c11dfaca5263bfddaf",
  "cid": "QmV1dfcf54184772144b145b987d85f5eb12644a6529",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286639,
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
      "evaluated_at": 1760286639
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
  "sig": "7c6ad6a1e12b1e61666e471ac1a8483f441196262d615299838bcf10f503c13e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009595535562
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285763, 'matching_hash': '052e7693e8a3f40d'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285764, 'matching_hash': 'ef2983ea6f6c1303'}}}