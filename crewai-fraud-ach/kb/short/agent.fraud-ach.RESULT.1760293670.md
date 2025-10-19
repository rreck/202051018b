```json
{
  "id": "31dd0e701c9039b8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293670,
  "host_pid": "9e6742732c60:1",
  "hash": "be25e21a5f555c033198bc4b91be5057e0289f0173237336a238927975d3d01f",
  "cid": "QmV1be25e21a5f555c033198bc4b91be5057e0289f01",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293670,
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
      "evaluated_at": 1760293670
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
  "sig": "ffa7cd7d74f5d621777aec202f980e0a2eab10de9b9c7a03e8a8f31144179762"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278705813
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 70189027, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285764, 'matching_hash': '628aaca406e38baa'}}}