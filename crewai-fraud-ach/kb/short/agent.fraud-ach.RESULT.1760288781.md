```json
{
  "id": "c67e9c021738c5ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288781,
  "host_pid": "9e6742732c60:1",
  "hash": "bb5d3034118241e782e00b1bf3fb531dfe5bb5cbf2d7630da646699bfdca4f76",
  "cid": "QmV1bb5d3034118241e782e00b1bf3fb531dfe5bb5cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288781,
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
      "evaluated_at": 1760288781
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
  "sig": "afe99f0e01e09dc1544edcea0e883de7e415313c1a1836609dc3e6b0db2f19a2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591278492
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 12971504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285763, 'matching_hash': '3e8e4f28808ab222'}}}