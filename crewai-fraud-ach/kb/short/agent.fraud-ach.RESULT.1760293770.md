```json
{
  "id": "1527beb74f17ee32",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293770,
  "host_pid": "9e6742732c60:1",
  "hash": "93c4831eee25125c0a904dd4919da12de72737d84eae7dd3d55c986f9231f45e",
  "cid": "QmV193c4831eee25125c0a904dd4919da12de72737d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293770,
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
      "evaluated_at": 1760293770
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
  "sig": "e5760adcd94a1ab8f9d3e22b9d035133c08045dc20c9312b2279246105f7efd1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599719457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 41817375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '97e4873137c26cd1'}}}